resource "google_compute_network" "vpc_network" {
  name = "${var.environment}-vpc"
  project = "${var.project_id}-${var.environment}"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet" {
  name          = "${var.environment}-subnet"
  ip_cidr_range = var.subnet_cidr
  region        = var.region
  network       = google_compute_network.vpc.id
  project       = "${var.project_id}-${var.environment}"
}