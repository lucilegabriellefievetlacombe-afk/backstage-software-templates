# Documents for ${{values.name}}

* component uid : ${{values.uid}}
* deployment environements : ${{values.environements}}
* owner: ${{values.owner}}

### This application has 5 endpoints:
- `/` home
- `api/json/v1/info` to get infos
- `api/html/v1/grettings` grettings in html
- `api/json/v1/grettings` grettings in json
- `api/json/v1/healthz` get health status in json

Here you could expand on what each of these endpoints do.

# How to access the app?

You can access the app by accessing this URL: 
`${{values.uid}}.test.com/api/v1/healthz` 