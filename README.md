# Streamlib Library

A collection of catalogued media streams to be played with the [streamlib](https://github.com/streamlib/streamlib) meta-player

## Structure

All library TOML files are located under the [library](library) directory.

Utility scripts can be found in the [utils](utils) directory.

## Library Specification

Streamlib library files are nothing more than [TOML](https://github.com/toml-lang/toml) files which adhere to the following specification, given by example:

```toml
[groovesalad]
name = "Groove Salad"
description = "A nicely chilled plate of ambient/downtempo beats and grooves"
url = "http://somafm.com/groovesalad.pls"
tags = ["somafm", "radio", "ambient", "groove"]
http_header = "User-Agent: foo"
```

The only real requirement in a streamlib file is to have one or more top-level tables which at bare minimum includes a `url` key:

```toml
[secretagent]
url = "http://somafm.com/secretagent.pls"
```

All the other keys are used for indexing and querying upon playback, but are essentially optional.

Further fields might be added later on to the specification.

### Queries

In some cases, streams might be signed with timestamps or tokens and thus cannot be played from a static URL. Don't worry, streamlib has you covered and supports these use-cases. Consider this example:

```toml
[secretstream]
name = "A secret stream"
url = "http://example.com/index.m3u8"

    [[secretstream.query]]
    name = "token"
    url = "http://example.com/tokenservice/"
    regex = 'token=(\d+)'
    json = 'tokens.0.token'
```

The example stream URL will fail and return e.g. a `403` status code unless given a proper token as a URL query parameter.

Prior to playing the stream URL, streamlib will make a request to the token service and fetch a new token. The token can be parsed in one of two ways:

 - A regular expression can be matched against the token service response, it must include one capture sequence that captures the actual token. In the example, if a textual response `token=1234` is given then the value `1234` will be captured.
 - A JSON query can be matched against a valid JSON response. The syntax supported includes only object names, and array indices. In the example, the JSON response object `{"tokens": ["token": "1234"]}` will be parsed and queried to extract the same value `1234`.

The final value will be added to the stream URL as a query argument `token`, yielding the final stream URL of `http://example.com/index.m3u8?token=1234`

Note that multiple query values can be provided if neccesary.

This specification should support most dynamic token generation services, but further feedback would be much appreciated on this subject.
