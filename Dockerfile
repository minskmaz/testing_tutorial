# To build:
# docker build -t python2 .
#
# To test:
# docker run python2 echo 'hi'
#
# To run:
# docker run -i -t -v ${PWD}/code:/data/code python2  python -m doctest /data/code/my_program.py
#
# To run as an independent system:
# docker run -d -p 2222:22 -v ${PWD}/code:/data/code python2
# ssh -p 2222 admin@localhost

FROM mzdaniel/python2-pkg
CMD  ["/usr/local/bin/supervisord", "-n"]
