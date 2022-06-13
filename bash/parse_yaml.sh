#!/bin/bash

## Credits
# This function is taken from https://gist.github.com/pkuczynski/8665367

## Definition
# The function reads a YAML file from a bash script
# The output content maintains the structure of the yaml file

## Usage (in a main bash script)
# source <absolute_or_relative_path_from_bash>/parse_yaml.sh # include parse_yaml function
# eval $(parse_yaml <absolute_or_relative_path_from_bash>/<file_name>.yaml "<opt_prefix>_") # read desired yaml file
# echo $<opt_prefix>_<yaml_variable_with_tree_structure> # access yaml content

## Warnings
# The indent in the yaml file must be 2 spaces exactly

parse_yaml() {
   local prefix=$2
   local s='[[:space:]]*' w='[a-zA-Z0-9_]*' fs=$(echo @|tr @ '\034')
   sed -ne "s|^\($s\)\($w\)$s:$s\"\(.*\)\"$s\$|\1$fs\2$fs\3|p" \
        -e "s|^\($s\)\($w\)$s:$s\(.*\)$s\$|\1$fs\2$fs\3|p"  $1 |
   awk -F$fs '{
      indent = length($1)/2;
      vname[indent] = $2;
      for (i in vname) {if (i > indent) {delete vname[i]}}
      if (length($3) > 0) {
         vn=""; for (i=0; i<indent; i++) {vn=(vn)(vname[i])("_")}
         printf("%s%s%s=\"%s\"\n", "'$prefix'",vn, $2, $3);
      }
   }'
}
