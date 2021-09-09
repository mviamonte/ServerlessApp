terraform {
  backend "s3" {
    bucket = "mvawsbucket"
    key    = "terraform_start/terraform_state.tfstate"
    region = "us-east-1"
  }
}