resource "google_service_account" "gke_service" {
  account_id = var.account_id
  project = var.project_id
  display_name = var.display_name
}

resource "google_project_iam_member" "gke_sa_iam_roles" {
  for_each = toset(var.roles)
  project  = "${var.project_id}-${var.environment}"
  role     = each.value
  member   = "serviceAccount:${google_service_account.gke_service.email}"
}