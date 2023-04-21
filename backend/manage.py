#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import configparser
import logging
from django.core.management.utils import get_random_secret_key

logger = logging.getLogger(__name__)

# config section for docker
if not os.path.isdir("/config"):
    os.makedirs("/config", exist_ok=True)

CONFIG_PATH = "/config/config.ini"
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# Init django ini file
if not config.has_section("settings"):
    config.add_section("settings")

# create new secret key
if not config.has_option("settings", "SECRET_KEY"):
    # config parser does not like single '%' in strings see https://docs.python.org/3/library/configparser.html#configparser.BasicInterpolation
    config.set("settings", "SECRET_KEY", get_random_secret_key().replace("%", ""))

    # write to the config file
    with open(CONFIG_PATH, "w") as f:
        config.write(f)


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bespeak.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
