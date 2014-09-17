# To build:
# docker build -t python2 .
#
# To test:
# docker run python2 echo 'hi'
#
# To run:
# docker run -i -t -v ${PWD}/code:/data/code python2  python -m doctest /data/code/my_program.py

FROM mzdaniel/python2-pkg
