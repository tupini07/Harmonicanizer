help:
    just --list

test:
    pytest

make-web:
    cd web; brython-cli --make_dist
