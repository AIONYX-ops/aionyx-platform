resource "kubernetes_namespace" "monitoring" {
  metadata {
    name = "monitoring"
  }
}

resource "helm_release" "prometheus" {
  name       = "prometheus"
  repository = "https://prometheus-community.github.io/helm-charts"
  chart      = "kube-prometheus-stack"
  namespace  = kubernetes_namespace.monitoring.metadata[0].name
  timeout    = 900 # 15 minutes for local pull
  
  set {
    name  = "grafana.enabled"
    value = "true"
  }

  # Kind-specific fixes: Disable scraping of components Kind handles internally/differently
  set {
    name  = "kubeStateMetrics.enabled"
    value = "true"
  }
  
  set {
    name  = "nodeExporter.enabled"
    value = "true"
  }

  set {
    name  = "kubeEtcd.enabled"
    value = "false"
  }

  set {
    name  = "kubeControllerManager.enabled"
    value = "false"
  }

  set {
    name  = "kubeScheduler.enabled"
    value = "false"
  }

  set {
    name  = "prometheus.prometheusSpec.serviceMonitorSelectorNilUsesHelmValues"
    value = "false"
  }
  
  # Ensure the cluster is ready before deploying
  depends_on = [kind_cluster.aionyx_cluster]
}
