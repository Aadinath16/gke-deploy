# Project ID where resources will be deployed
variable "project_id" {
  description = "The GCP project ID where Terraform will manage resources"
  type        = string
}

# Region for regional resources
variable "region" {
  description = "The GCP region to deploy resources into"
  type        = string
  default     = "us-central1"
}

# Zone for zonal resources
variable "zone" {
  description = "The GCP zone for zonal resources"
  type        = string
  default     = "us-central1-a"
}

# Environment (dev, uat, prod)
variable "environment" {
  description = "The environment to deploy (dev/uat/prod)"
  type        = string
}
