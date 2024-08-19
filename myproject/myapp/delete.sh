echo "In the delete bash script"

#!/bin/bash

# MySQL connection details
DB_HOST="localhost"
DB_USER="root"
DB_PASSWORD="root"
DB_NAME="your_database"

## Function to delete namespace and update status
#delete_namespace() {
#    local namespace_name="$1"
#
#    # Connect to MySQL and run the DELETE and UPDATE queries
#    mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" <<EOF
#    -- Delete the row from namespace_status where namespace matches
#    DELETE FROM namespace_status WHERE namespace = '$namespace_name';
#
#    -- Update the status of the namespace in the namespace table to 'Available'
#    UPDATE namespace_pool
#    SET status = 'Available', allocation_lock = 'NO'
#    WHERE namespace = '$namespace_name';
#EOF
#
#    if [ $? -eq 0 ]; then
#        echo "Deleted namespace '$namespace_name' from namespace_status and updated status to 'Available'."
#    else
#        echo "Error during namespace deletion."
#    fi
#}
#
## Usage example
#delete_namespace "o-devops-bsf1"
