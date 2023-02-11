# ACM certificate should always be in us-east-1 for Cloudfront

Since cloudfront is a global service, the certificate attached to it should always be in `us-east-1`.

For other services, that are regional, like Layer 7 - ALBs (Application Load Balancers), the region of SSL certificate depends on the region where ALB is placed.
