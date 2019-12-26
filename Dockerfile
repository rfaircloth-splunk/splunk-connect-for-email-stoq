FROM punchcyber/stoq:v2
LABEL maintainer="marcus@punchcyber.com"

COPY splunk /tmp/splunk
COPY yara /home/stoq/yara
RUN mkdir -p /var/mailsink; chmod 766 /var/mailsink
RUN cd /tmp; stoq install splunk