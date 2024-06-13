![ITFY](https://github.com/pointless-code/is-it-friday-yet/assets/18129171/1b72bdcc-daca-426c-84c8-e1065f9bbd4b)

## About IsItFridayYet?

A .less docker container helps you track the coolest days of the week.

## Pull from docker

```bash
docker pull pointlesscode/is-it-friday-yet:latest
docker run --rm pointlesscode/is-it-friday-yet

// pass your own timezone (default is Europe/London)
docker run --rm -e TZ=America/New_York pointlesscode/is-it-friday-yet
```

## Build it yourself
- clone the project and cd to folder
- build and run the image
```bash
docker pull is-it-friday-yet:latest
docker run --rm is-it-friday-yet

// pass your own timezone (default is Europe/London)
docker run --rm -e TZ=America/New_York is-it-friday-yet
```

## Social

<a href="https://pointlesscode.dev/">.less</a><br>
<a href="https://www.instagram.com/pointlesscode">Instagram</a><br>
<a href="https://x.com/pointlessCodes">Twitter</a><br>
<a href="https://github.com/pointless-code">GitHub</a><br>
<a href="https://hub.docker.com/u/pointlesscode">DockerHub</a>

## License

The project is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
