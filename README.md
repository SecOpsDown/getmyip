# getmyip
Simple lambdas and an API Gateway configuration to return back the requesters IP in HTML or JSON. Use to replace whatismyip.com services as an example. 

**NOTE: There is no security on this, its an open endpoint so anyone can use it, you can use authorizaton keys or within the lambda do additional filters.

# Install

Create two lambdas getmyip_html and getmyip_json, and upload the correct script to each. Afterwards go to the API Gateway and upload the apigateway_swagger.txt.

# Modifications
You can modify the hostname post install, however, you should modify the ARNLAMBDA_(?) with the correct ARNs for their respective lambdas.

# Import additional headers
To Import additional headers, modify the request template and you can modify the return in the lambdas.