import argparse
import logging
import uvicorn
from main import app

def create_parser():
    parser = argparse.ArgumentParser(description="Start the FastAPI server.")
    parser.add_argument("--port", type=int, default=8000, help="Port to listen on (default: 8000).")
    parser.add_argument(
        "--log-level",
        type=str,
        default="info",
        choices=["debug", "info", "warning", "error", "critical"],
        help="Logging level (default: info)."
    )
    parser.add_argument("--log-file", type=str, help="Optional file name to write logs to (default: console).")
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    # Configure logging
    log_params = {
        "level": args.log_level.upper(),
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    }
    if args.log_file:
        log_params["filename"] = args.log_file

    logging.basicConfig(**log_params)
    logger = logging.getLogger(__name__)
    logger.info(f"Starting server on port {args.port} with log level {args.log_level}")

    if args.log_file:
        # If we are logging to a file, we want uvicorn logs there too.
        # We'll configure uvicorn loggers to propagate to the root logger
        # and remove their default handlers to avoid duplicate/console output.
        for logger_name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
            uv_logger = logging.getLogger(logger_name)
            uv_logger.handlers = []
            uv_logger.propagate = True

        # Pass log_config=None to prevent uvicorn from reconfiguring logging
        uvicorn.run(app, host="0.0.0.0", port=args.port, log_config=None, log_level=args.log_level.lower())
    else:
        # Standard uvicorn run for console output
        uvicorn.run(app, host="0.0.0.0", port=args.port, log_level=args.log_level.lower())

if __name__ == "__main__":
    main()
