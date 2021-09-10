resource "aws_s3_bucket" "cb" {
  bucket = "cbs3staticsite"
  acl    = "public-read"
  policy = file("../policy.json")

  website {
    index_document = "index.html"
    error_document = "error.html"
    routing_rules = <<EOF
[{
    "Condition": {  
        "KeyPrefixEquals": "putobject.html"
    },
    "Redirect": {
        "Hostname": "www.google.com"
    }
}]
EOF
  }
}
