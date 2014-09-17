# To build:
# docker build -t buildbot .
#
# To run:
# docker run -d -p 2222:22 -p 8010:8010 -v ${PWD}/code:/data/buildbot/code buildbot
# ssh -p 2222 admin@localhost

FROM mzdaniel/buildbot-pkg
ADD  master.cfg /data/buildbot/master/master.cfg
CMD  ["/usr/local/bin/supervisord", "-n"]
