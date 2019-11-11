# jobmonitorservice
## Usage
All responses will have the form
```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all devices

**Definition**

`GET /modulelog/`

**Response**

- `200 OK` on success

```json
[
    {
        "job_id": "c569c316-042a-11ea-9a9f-362b9e155667",
        "app_name": "Hello App",
        "state": "STARTED",
        "date_created": "2019-11-11"
    }
]
```

### Registering a new device

**Definition**

`POST /modulelog`

**Arguments**

- `"job_id":string` a globally unique identifier for this device
- `"app_name":string` a friendly name for this device
- `"state":string` the state of an app [STARTED, FINISHED, ERROR]
- `"date_created":string` the date when an app is created

If a job with the given job_id already exists, the existing job will be overwritten.

**Response**

- `201 Created` on success

```json
{
     "job_id": "c569c316-042a-11ea-9a9f-362b9e155667",
     "app_name": "Hello App",
     "state": "STARTED",
     "date_created": "2019-11-11"
}

```

## Lookup device details

`GET /modulelog/<job_id>`

**Response**

- `404 Not Found` if the device does not exist
- `200 OK` on success

```json
{
     "job_id": "c569c316-042a-11ea-9a9f-362b9e155667",
     "app_name": "Hello App",
     "state": "STARTED",
     "date_created": "2019-11-11"
}
```

## Delete a device

**Definition**

`DELETE /modulelog/<job_id>`

**Response**

- `404 Not Found` if the device does not exist
- `204 No Content` on success