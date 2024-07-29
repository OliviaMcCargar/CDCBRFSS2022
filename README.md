

# CDCBRFSS Analysis Overview

A personal project showcasing the building of a bespoke data pipeline from raw ingestion of the data available on the CDC website to functional data and a useable dictionary for analysis and dashboarding.

### Olivia McCargar

I am a solo dev with an MS in Computer Science with a focus on data anlytics. My primary work background is in higher education, but I am hoping to pivot to doing data analysis in either public health or healthcare with a goal towards data engineering. If yo uare interested in seeing more of my work, please visit my website: [http://www.oliviamccargar.com](http://www.oliviamccargar.com)

### Building The PostgreSQL Database
*Lightly updated script and process from [Vishal Sharma](https://medium.com/@vishal.sharma./run-postgresql-and-pgadmin-using-docker-compose-34120618bcf9)*

- [Docker](https://docs.docker.com/get-docker/) must be installed and functional on your system.
- Open a terminal and navigate to the top level CDCBRFSS folder
- Create or edit a .env file 

```
nano .env
```

- Make sure it includes at least the following arguments (you can set these values as desired):

```
# Database
POSTGRES_DB=postgres_database_name
POSTGRES_USER=postgres_database_user
POSTGRES_PASSWORD=password

# pgadmin
PGADMIN_DEFAULT_EMAIL=pgadmin_email
PGADMIN_DEFAULT_PASSWORD=pgadmin_password
```

- Press <kbd>Ctrl</kbd> + <kbd>X</kbd> then <kbd>Y</kbd> to save
- In the terminal, execute:

```
docker compose up -d
```

- pgadmin should now be accessible in your browser at [http://localhost:8888/](http://localhost:8888/)
- Connect to the database in pgadmin, the name should be "db" on port 5432 with the username and password specified in your .env file:

![image info](./images/pgadmin%20connect.png)

### Loading the Data

TBD