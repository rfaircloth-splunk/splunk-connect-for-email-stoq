#Splunk Connect for Syslog (SC4S) by Splunk, Inc.
#
#To the extent possible under law, the person who associated CC0 with
#Splunk Connect for Syslog (SC4S) has waived all copyright and related or neighboring rights
#to Splunk Connect for Syslog (SC4S).
#
#You should have received a copy of the CC0 legalcode along with this
#work.  If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.
FROM registry.access.redhat.com/ubi8/python-36

USER root
RUN cd /tmp ;\
    dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y; \
    dnf update -y ;\
    dnf install -y postfix mailx perl supervisor rsyslog nc && \
    dnf clean all


COPY --from=aelsabbahy/goss:v0.3.9 /goss /goss
COPY goss.yaml /etc/goss.yaml
COPY --from=hairyhenderson/gomplate:v3.6.0-slim /gomplate /bin/gomplate

COPY entrypoint.sh /

EXPOSE 25/tcp
EXPOSE 587/tcp
EXPOSE 8080/tcp

RUN sed -i -e "s/^nodaemon=false/nodaemon=true/" /etc/supervisord.conf
RUN sed -i -e 's/inet_interfaces = localhost/inet_interfaces = all/g' /etc/postfix/main.cf
RUN mkdir -p /var/run/supervisor/

COPY etc/ /etc/
COPY stoqsink.py /bin/stoqsink.py
RUN chmod 755 /bin/stoqsink.py

RUN newaliases

ENTRYPOINT ["/entrypoint.sh"]

HEALTHCHECK --interval=1s --timeout=6s CMD /goss/goss -g /etc/goss.yaml serve