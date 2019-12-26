#   Copyright 2014-2018 PUNCH Cyber Analytics Group
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
Overview
========

Save results to Splunk

"""
import json
import certifi
from splunk_http_event_collector import http_event_collector

from datetime import datetime
from typing import Optional, Dict
from configparser import ConfigParser

from stoq import helpers
from stoq.plugins import ConnectorPlugin
from stoq.data_classes import StoqResponse


class SplunkPlugin(ConnectorPlugin):
    def __init__(self, config: ConfigParser, plugin_opts: Optional[Dict]) -> None:
        super().__init__(config, plugin_opts)

        self.splunk_index = 'stoq'
        self.splunk_host = None
        self.splunk_token = None
        self.splunk_port = "8088"
        self.splunk_tls = True
        self.splunk_timeout = 60
        self.splunk_max_retries = 10
        self.hec = None

        if plugin_opts and 'splunk_host' in plugin_opts:
            self.splunk_host = plugin_opts['splunk_host']
        elif config.has_option('options', 'splunk_host'):
            self.splunk_host = config.get('options', 'splunk_host')

        if plugin_opts and 'splunk_tls' in plugin_opts:
            self.splunk_tls = plugin_opts['splunk_tls']
        elif config.has_option('options', 'splunk_tls'):
            self.splunk_tls = config.get('options', 'splunk_tls')

        if plugin_opts and 'splunk_tls' in plugin_opts:
            self.splunk_tls = plugin_opts['splunk_tls']
        elif config.has_option('options', 'splunk_tls'):
            self.splunk_tls = config.get('options', 'splunk_tls')

        if plugin_opts and 'splunk_token' in plugin_opts:
            self.splunk_token = plugin_opts['splunk_token']
        elif config.has_option('options', 'splunk_token'):
            self.splunk_token = config.get('options', 'splunk_token')

        if plugin_opts and 'splunk_timeout' in plugin_opts:
            self.splunk_timeout = int(plugin_opts['splunk_timeout'])
        elif config.has_option('options', 'splunk_timeout'):
            self.splunk_timeout = int(config.get('options', 'splunk_timeout'))

        if plugin_opts and 'splunk_retry' in plugin_opts:
            self.splunk_retry = plugin_opts['splunk_retry']
        elif config.has_option('options', 'splunk_retry'):
            self.splunk_retry = config.getboolean('options', 'splunk_retry')

        if plugin_opts and 'splunk_max_retries' in plugin_opts:
            self.splunk_max_retries = int(plugin_opts['splunk_max_retries'])
        elif config.has_option('options', 'splunk_max_retries'):
            self.splunk_max_retries = int(config.get('options', 'splunk_max_retries'))

        if plugin_opts and 'splunk_index' in plugin_opts:
            self.splunk_index = plugin_opts['splunk_index']
        elif config.has_option('options', 'splunk_index'):
            self.splunk_index = config.get('options', 'splunk_index')

    def save(self, response: StoqResponse) -> None:
        """
        Save results to Splunk

        """

        self._connect()

        payload = {}
        payload.update({"index": self.splunk_index })
        payload.update({"sourcetype": "stoq"})
        payload.update({"source": "stoq"})
        payload.update({"host": "stoq"})

        payload.update({"event": f'{helpers.dumps(response, compactly=True)}\n' })

        self.hec.sendEvent(payload)

    def _connect(self):
        """
        Connect to an splunk instance

        """
        if not self.hec:
            self.hec = http_event_collector(
                self.splunk_token,
                self.splunk_host,
                self.http_event_port
            )
            #self.hec.popNullFields = True