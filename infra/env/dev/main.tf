module "network" {
  source      = "../../modules/network"
  project_id  = var.project_id
  region      = var.region
  environment = var.environment
  subnet_cidr = "10.0.0.0/24"
}


# module "gke" {
#   source      = "../../modules/gke"
#   project_id  = var.project_id
#   region      = var.region
#   environment = var.environment

#   vpc_name    = module.network.vpc_name
#   subnet_name = module.network.subnet_name
# }

module "service-account" {
  source = "../../modules/service-account"
  project_id = var.project_id
  roles = [
    "roles/container.nodeServiceAccount",
    "roles/compute.instanceAdmin.v1",
    "roles/logging.logWriter",
    "roles/monitoring.metricWriter"
  ]
  environment = var.environment
  account_id = "dev-node-sa"
  display_name = "Dev Node Service Account"

}