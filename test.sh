### Commands to set up CodaLab (first run)
#cl new <insert_your_codalab_name>-KeepinItReal
#cl work <insert_your_codalab_name>-KeepinItReal
#cl upload src -d "KeepinItReal src code"
#cl add bundle dsga1003-project-review//train.csv
#cl add bundle dsga1003-project-review//dev.csv

### CodaLab arguments
CODALAB_ARGS="cl run"

# Name of bundle (can customize however you want)ls
CODALAB_ARGS="$CODALAB_ARGS --name KeepinItReal-test.py"
# Docker image (default: codalab/default-cpu)
CODALAB_ARGS="$CODALAB_ARGS --request-docker-image codalab/default-gpu"
# Explicitly ask for a worker with at least one GPU
CODALAB_ARGS="$CODALAB_ARGS --request-gpus 1"
# Control the amount of RAM your run needs
#CODALAB_ARGS="$CODALAB_ARGS --request-memory 5g"
# Kill job after this many days (default: 1 day)
CODALAB_ARGS="$CODALAB_ARGS --request-time 2d"

# Bundle dependencies
CODALAB_ARGS="$CODALAB_ARGS :src"        # Code

### Command to execute (these flags can be overridden) from the command-line
CMD="python src/test.py debug"
# Runs can feel free to output to the current directory, which is in the bundle
#CMD="$CMD --outputdir ."

# Pass the command-line arguments through to override the above
if [ -n "$1" ]; then
  CMD="$CMD $@"
fi

# Create the run on CodaLab!
FINAL_COMMAND="$CODALAB_ARGS '$CMD'"
echo $FINAL_COMMAND
exec bash -c "$FINAL_COMMAND"
