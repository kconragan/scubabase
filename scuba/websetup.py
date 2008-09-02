"""Setup the Scuba application"""
import logging

from scuba.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup scuba here"""
    load_environment(conf.global_conf, conf.local_conf)
