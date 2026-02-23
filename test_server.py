import pytest
from server import create_parser

def test_parser_defaults():
    parser = create_parser()
    args = parser.parse_args([])
    assert args.port == 8000
    assert args.log_level == "info"
    assert args.log_file is None

def test_parser_custom_port():
    parser = create_parser()
    args = parser.parse_args(["--port", "9000"])
    assert args.port == 9000

def test_parser_valid_log_levels():
    parser = create_parser()
    for level in ["debug", "info", "warning", "error", "critical"]:
        args = parser.parse_args(["--log-level", level])
        assert args.log_level == level

def test_parser_invalid_log_level():
    parser = create_parser()
    # argparse raises SystemExit when an invalid choice is provided
    with pytest.raises(SystemExit):
        parser.parse_args(["--log-level", "invalid"])

def test_parser_custom_log_file():
    parser = create_parser()
    args = parser.parse_args(["--log-file", "test.log"])
    assert args.log_file == "test.log"

def test_parser_all_custom():
    parser = create_parser()
    args = parser.parse_args(["--port", "9000", "--log-level", "debug", "--log-file", "test.log"])
    assert args.port == 9000
    assert args.log_level == "debug"
    assert args.log_file == "test.log"
