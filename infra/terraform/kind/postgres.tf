resource "kubernetes_namespace" "storage" {
  metadata {
    name = "storage"
  }
}

resource "helm_release" "postgres" {
  name       = "aionyx-db"
  repository = "https://charts.bitnami.com/bitnami"
  chart      = "postgresql"
  namespace  = kubernetes_namespace.storage.metadata[0].name
  version    = "12.12.10"

  set {
    name  = "auth.username"
    value = "aionyx"
  }

  set {
    name  = "auth.password"
    value = "aionyx_secret_123"
  }

  set {
    name  = "auth.database"
    value = "aionyx_telemetry"
  }

  set {
    name  = "primary.persistence.size"
    value = "10Gi"
  }

  # Ensure the cluster is ready
  depends_on = [kind_cluster.aionyx_cluster]
}
