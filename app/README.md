# Response structure

json -> {
   message: string,
   success: boolean,
   data: object | null
 }

controllers must define the code returned by the service
as status code of the http response.
