from flask import request, json, Response, Blueprint
from ..models.JobModel import JobModel, JobSchema
from sqlalchemy.dialects.postgresql import UUID

job_api = Blueprint('users', __name__)
job_schema = JobSchema()

@job_api.route('/', methods=['POST'])
def create():
    """
    Create Job Function
    """
    req_data = request.get_json()
    data, error = job_schema.load(req_data)
    if error:
        return custom_response(error, 404)
    job = JobModel(data)
    job.save()

    job_message = job_schema.dump(job)

    return custom_response(job_message, 201)

@job_api.route('/', methods=['GET'])
def get_all():
  jobs = JobModel.get_all_jobs()
  ser_users = job_schema.dump(jobs, many=True)
  return custom_response(ser_users, 200)

@job_api.route('/<string:job_id>', methods=['GET'])
def get_a_job(job_id):
    """
    Get a single user
    """
    job = JobModel.get_one_job(job_id)
    if not job:
        return custom_response({'Error': 'Job Not Found'}, 404)

    job_message = job_schema.dump(job, many=True)
    return custom_response(job_message, 200)

@job_api.route('/<string:job_id>', methods=['PUT'])
def update_all():
  """
  Updates all with the given job_id
  """
  req_data = request.get_json()
  jobs = JobModel.get_one_job(job_id)
  if not jobs:
      return custom_response({'Error': 'Job Not Found'}, 404)

  data, error = job_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)

  for job in jobs:
      job.update(data)
      job_message = job_schema.dump(job)

  return custom_response(job_message, 200)

@job_api.route('/<string:job_id>', methods=['DELETE'])
def delete(job_id):
    """
    Delete jobs based on the given job_id
    :param job_id:
    :return:
    """
    job = JobModel.get_one_job(job_id)
    if not job:
        return custom_response({'Error':'Job Not Found'}, 404)

    JobModel.query.filter(JobModel.job_id == job_id).delete()

    return custom_response({'Message': 'Deleted'}, 204)

def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )