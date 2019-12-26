# Splunk

[stoQ](https://stoq-framework.readthedocs.io/en/latest/index.html) plugin that saves results to [Splunk](https://www.splunk.com)


## Plugin Classes

- [Connector](https://stoq-framework.readthedocs.io/en/latest/dev/connectors.html)

## Configuration

All options below may be set by:

- [plugin configuration file](https://stoq-framework.readthedocs.io/en/latest/dev/plugin_overview.html#configuration)
- [`stoq` command](https://stoq-framework.readthedocs.io/en/latest/gettingstarted.html#plugin-options)
- [`Stoq` class](https://stoq-framework.readthedocs.io/en/latest/dev/core.html?highlight=plugin_opts#using-providers)

### Options

- `splunk_host` [str]: Splunk HEC URI

- `splunk_token` [str]: Splunk HEC TOKEN

- `splunk_options` [json]: options for connection)

> Example: `es_options = {"port": 443, "use_ssl": true, "verify_certs": true}`

- `splunk_index` [str]: Index name to use for saving results

- `splunk_timeout` [int]: Time to wait for ES operations to complete before timing out

- `splunk_retry` [True/False]: Should the plugin try again if the operation fails?

- `splunk_max_retries` [int]: Number of retries to attempt before a timeout occurrs

