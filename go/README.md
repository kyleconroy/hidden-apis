# Go

    go get code.google.com/p/go.net/proxy

```go
package main

import (
	"code.google.com/p/go.net/proxy"
	"net/http"
  "log"
  "io/ioutil"
)

func main() {
	dialer, err := proxy.SOCKS5("tcp", "127.0.0.1:9150", nil, proxy.Direct)

	if err != nil {
		log.Fatal(err)
	}

	tr := &http.Transport{Dial: dialer.Dial}
	httpClient := &http.Client{Transport: tr}

	resp, err := httpClient.Get("http://3g2upl4pq6kufc4m.onion/?q=define+ostensibly&format=json")

	if err != nil {
		log.Fatal(err)
	}

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)

	if err != nil {
		log.Fatal(err)
	}

	log.Println(string(body))
}
```

