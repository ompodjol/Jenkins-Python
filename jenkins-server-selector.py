#!/bin/python

#############################################
##### Author : Jolly Jae Ompod          #####
##### Date Created: 2019-11-14          #####
#############################################

import jenkins
import json


class ServerName:


        def __init__(self, serverAddress, jobPipelineName):
                self.serverAddress = serverAddress
                self.jobPipelineName = jobPipelineName

        def server_name(self):
                print "JENKINS SERVER ADDRESS : ", self.serverAddress

        def job_name(self):
                print "PIPELINE JOB NAME : ", self.jobPipelineName

        def job_count():
                print "SERVER JOB COUNT: ", jobs_count()

	def last_build_job_number():
        	get_job_info_number = server.get_job_info('%s' % jobPipelineName)['lastBuild']['number']
        	print "LAST JOB BUILD NUMBER : ", get_job_info_number

	def last_build_job_name():
        	get_job_info_number = server.get_job_info('%s' % jobPipelineName)['lastBuild']['number']
        	pipeline_job_info_lastBuild_displayName = server.get_build_info('%s' % jobPipelineName, get_job_info_number) ['displayName']
        	print "LAST JOB BUILD NAME : ", pipeline_job_info_lastBuild_displayName

	def last_build_job_result():
        	get_job_info_number = server.get_job_info('%s' % jobPipelineName)['lastBuild']['number']
        	pipeline_job_info_lastBuild_result = server.get_build_info('%s' % jobPipelineName, get_job_info_number) ['result']
        	print "LAST JOB BUILD RESULT : ", pipeline_job_info_lastBuild_result

	def last_successful_build_job_number():
        	get_successful_job_info_number = server.get_job_info('%s' % jobPipelineName)['lastSuccessfulBuild']['number']
        	print "LAST SUCCESSFUL JOB BUILD NUMBER : ", get_successful_job_info_number

	def last_successful_build_job_name():
        	get_successful_job_info_number = server.get_job_info('%s' % jobPipelineName)['lastSuccessfulBuild']['number']
        	pipeline_job_info_lastSuccessfulBuild_displayName = server.get_build_info('%s' % jobPipelineName, get_successful_job_info_number) ['displayName']
        	print "LAST SUCCESSFUL JOB BUILD NUMBER : ", pipeline_job_info_lastSuccessfulBuild_displayName

	def last_successful_build_job_result():
        	get_job_info_number = server.get_job_info('%s' % jobPipelineName)['lastSuccessfulBuild']['number']
        	pipeline_job_info_lastSuccessfulBuild_result = server.get_build_info('%s' % jobPipelineName, get_job_info_number) ['result']
        	print "LAST SUCCESSFUL JOB BUILD RESULT(expected is {SUCCESS}) : ", pipeline_job_info_lastSuccessfulBuild_result

	def last_unsuccessful_build_job_number():
        	get_unsuccessful_job_info_number = server.get_job_info('%s' % jobPipelineName)['lastUnsuccessfulBuild']['number']
        	print "LAST UNSUCCESSFUL JOB BUILD NUMBER : ", get_unsuccessful_job_info_number

	def last_unsuccessful_build_job_name():
        	get_unsuccessful_job_info_number = server.get_job_info('%s' % jobPipelineName)['lastUnsuccessfulBuild']['number']
        	pipeline_job_info_lastUnsuccessfulBuild_displayName = server.get_build_info('%s' % jobPipelineName, get_unsuccessful_job_info_number) ['displayName']
        	print "LAST UNSUCCESSFUL JOB BUILD NUMBER : ", pipeline_job_info_lastUnsuccessfulBuild_displayName

	def last_unsuccessful_build_job_result():
        	get_job_info_number = server.get_job_info('%s' % jobPipelineName)['lastUnsuccessfulBuild']['number']
        	pipeline_job_info_lastUnsuccessfulBuild_result = server.get_build_info('%s' % jobPipelineName, get_job_info_number) ['result']
        	print "LAST UNSUCCESSFUL JOB BUILD RESULT(expected is {FAILURE}) : ", pipeline_job_info_lastUnsuccessfulBuild_result

	def last_failed_build_job_number():
        	get_failed_job_info_number = server.get_job_info('%s' % jobPipelineName)['lastFailedBuild']['number']
        	print "LAST FAILED JOB BUILD NUMBER : ", get_failed_job_info_number

	def last_failed_build_job_name():
        	get_failed_job_info_number = server.get_job_info('%s' % jobPipelineName)['lastFailedBuild']['number']
        	pipeline_job_info_lastFailedBuild_displayName = server.get_build_info('%s' % jobPipelineName, get_failed_job_info_number) ['displayName']
        	print "LAST FAILED JOB BUILD NUMBER : ", pipeline_job_info_FailedBuild_displayName

	def last_failed_build_job_result():
        	get_job_info_number = server.get_job_info('%s' % jobPipelineName)['lastFailedBuild']['number']
        	pipeline_job_info_lastFailedBuild_result = server.get_build_info('%s' % jobPipelineName, get_job_info_number) ['result']
        	print "LAST FAILED JOB BUILD RESULT(expected is {FAILURE}) : ", pipeline_job_info_lastFailedBuild_result

	def job_health_report_score():
        	get_job_health_info = server.get_job_info('%s' % jobPipelineName)['healthReport']
        	print "HEALTH JOB PERCENTAGE(%) : ", get_job_health_info[0]['score']

	def job_health_report_description():
        	get_job_health_info = server.get_job_info('%s' % jobPipelineName)['healthReport']
        	print "HEALTH JOB DESCRIPTION: ", get_job_health_info[0]['description']

