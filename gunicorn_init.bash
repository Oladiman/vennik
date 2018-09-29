
# NAME="unik"                                                   # Name of the application
# DJANGODIR=/home/oluwadamilola/Documents/unik/                 # Django project directory
# SOCKFILE=/home/oluwadamilola/Documents/unik/ .venvs/unik/run/gunicorn.sock     # We will communicate using this unix socket
# USER=oluwadamilola                                              # the user to run as
# GROUP=oluwadamilola                                             # the group to run as
# NUM_WORKERS=3                                                   # how many worker processes shoul Gunicorn spawn
# DJANGO_SETTINGS_MODULE=unik.settings.production               # which settings file should Django use
# DJANGO_WSGI_MODULE=unik.wsgi                                  # WSGI module name
# echo "Starting $NAME as `whoami`"

# # Activate the virtual environment

# cd $DJANGODIR
# source /home/oluwadamilola/Documents/unik.venvs/unik/bin/activate
# export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
# export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# # Create the run directory if it doesn't exsist

# RUNDIR=$(dirname $SOCKFILE)
# test -d $RUNDIR || mkdir -p $RUNDIR

# # Start yout Django Unicorn
# # Programs meant to be run under supervisor should not daemonize themselves (do not use daemon)

# exec gunicorn ${DJANGO_WSGI_MODULE}:application \
#   --name $NAME \
#   --workers $NUM_WORKERS \
#   --user=$USER --group=$GROUP \
#   --bind=unix:$SOCKFILE \
#   --log-level=debug \
#   --log-file=-