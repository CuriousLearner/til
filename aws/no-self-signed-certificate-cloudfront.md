# No self-signed certificates in Cloudfront's SSL connection

If using cloudfront, then there will always be 2 SSL connections namely
`Visitor => Cloudfront` and then `Cloudfront => origin`. Both of these will be publically signed certificate. You can never use self-signed certificate.
