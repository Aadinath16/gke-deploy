module "gke" {
  source = "../../modules/gke"

}


module "network" {
  source = "../../modules/network"

}


module "service-account" {
  source = "../../modules/service-account"
  
}