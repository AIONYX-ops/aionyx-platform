terraform {
  required_providers {
    kind = {
      source  = "tehcyx/kind"
      version = "0.2.1"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.23.0"
    }
  }
}

provider "kind" {}

resource "kind_cluster" "aionyx_cluster" {
  name           = "aionyx-cluster"
  wait_for_ready = true

  kind_config {
    kind        = "Cluster"
    api_version = "kind.x-k8s.io/v1alpha4"

    node {
      role = "control-plane"
    }

    node {
      role = "worker"
    }
    
    node {
      role = "worker"
    }
  }
}

provider "kubernetes" {
  host                   = kind_cluster.aionyx_cluster.endpoint
  client_certificate     = kind_cluster.aionyx_cluster.client_certificate
  client_key             = kind_cluster.aionyx_cluster.client_key
  cluster_ca_certificate = kind_cluster.aionyx_cluster.cluster_ca_certificate
}
