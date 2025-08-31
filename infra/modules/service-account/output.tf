output "service_acc_name" {
    value = google_service_account.gke_service.email
}

output "service_acc_id" {
  value = google_service_account.gke_service.id
}