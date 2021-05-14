# Soccer Score APP

## Documentation
A customer wants a site where he can track his table soccer scores.

Customer requirements:
* Teams can be made up of a variable number of players, such as 1vs1, 2vs2 but
  also 1vs2 or 3vs3.

* The interface should be easy to use.

* There should be a ranking overview. A game won is worth 2 points, a draw
  worth 1 point and a lost game is worth 0 points.

* A team with 10 points in 3 matches is ranked lower than a person with 10
  points in 9 matches.

* It should be possible to give a team a special name.

* Ranking should happen at team level. Example: When there are three matches
  played as follows:
  - Ying vs. Ceesjan: 10-8
  - Ceesjan vs. Ying+John: 10-6
  - John vs. Ying: 4-4
  The ranking will look like this:
  - Ying:      3 points in 2 matches
  - Ceesjan:   2 points in 2 matches
  - John:      1 point  in 1 match
  - Ying+John: 0 points in 1 match

* The ranking should be made visual, fe. with a bar graph

* There should be an option for a game match maker: You select a number of
  people and the game will suggest teams with about the same strength (edge
  case: what kind of strength does a team with 0 games have?)

* Each team should have a summary page with some statistics such as games
  played, total points scored, total close victories

* There should be a week overview page, with statistics about the games played
  in the last week


#### Project Setup

Create a directory for the clone.

#### Installation

First You will need to install python version 3.6 or latest version
and django latest version.

#### Setup Virtual Environment

Create Virtual using python3 or follow below command

```
python3 -m venv <your-environment-name>
```

#### Install Requirements

For install requirements.txt use following command.

```
pip install -r requirements.txt
```

#### Run Project

Follow below commands to run the project.

```
python3 manage.py runserver
```

#### Run Migrations

Follow below commands to run migrations.

```
python3 manage.py migrate
```
