#!/bin/sh
while read -r line; do
    echo $line | grep . | grep -v '^#' && export $line;
done < /store/docker/local/vars.env

. /venv/bin/activate

export BANNER="$echo_red $(cat <<EOF | base64 -d
EOF
) $echo_normal"

alias add-column="xargs -d '\n' printf '%-50s\n'"

docker-help() {
    echo -e "$(cat <<EOF
build the base image from root dir of repo:
    docker build --no-cache -t service/store:1.0.0 -f ./docker/local/store/Dockerfile ./
in another terminal, to be able pdb.set_trace django
    docker-compose stop web && docker-compose run --service-ports web
in another terminal, a place to run tests, and django shell commands
    docker-compose exec web bash
EOF
)"

}

function yes_or_no {
    while true; do
        read -p "$* [y/n]: " yn
        case $yn in
            [Yy]*) return 0  ;;
            [Nn]*) echo "Aborted" ; return  1 ;;
        esac
    done
}

reset

echo -e "$BANNER"

_contains () {  # Check if space-separated list $1 contains line $2
  echo "$1" | tr ' ' '\n' | grep -F -x -q "$2"
}

get-ip() {
    for CONTAINER_HOST in $1;do
        ADD_PORT=
        ADD_PROTOCOL=
        check_store="store"
        if _contains "${check_store}" "${CONTAINER_HOST}"; then
          ADD_PROTOCOL="http://"
          ADD_PORT=":8000/ or try 127.0.0.1"
        fi
        check_db="postgres"
        if _contains "${check_db}" "${CONTAINER_HOST}"; then
          ADD_PROTOCOL="postgres://store:store@"
          ADD_PORT=":5432/"
        fi
        echo -e "$CONTAINER_HOST $ADD_PROTOCOL`getent hosts $CONTAINER_HOST | awk '{ print $1 }'`$ADD_PORT"
    done
}
paste <(add-column < <(
echo -e "bridged django"
echo
get-ip "postgres store"
))

cat <<EOF
to edit banner see: docker/local/env.sh
if you'd like to change the theme apt-get install nano and modify OSH_THEME in ~/.bashrc, also see:
    https://github.com/ohmybash/oh-my-bash
    https://github.com/ohmybash/oh-my-bash/tree/master/plugins
    https://github.com/ohmybash/oh-my-bash/wiki/Themes
Here's some things to try:
    apt-get install tree && tree ~/.oh-my-bash
    cat ~/.oh-my-bash/aliases/*
    ./manage.py help
    ./manage.py shell
    ./manage.py migrate
    docker-help
    Feel free to make a PR to update this at any time.
EOF