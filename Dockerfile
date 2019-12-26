FROM punchcyber/stoq:v2
LABEL maintainer="marcus@punchcyber.com"

COPY splunk /tmp/splunk
COPY yara /home/stoq/yara

RUN cd /tmp; stoq install splunk