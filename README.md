# Streamlib Library

A collection of curated media streams to be played with the [streamlib](https://github.com/streamlib/streamlib) CLI.

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
```

The only real requirement in a streamlib file is to have one or more top-level tables which at bare minimum includes a `url` key:

```toml
[secretagent]
url = "http://somafm.com/secretagent.pls"
```

All the other keys are used for indexing and querying upon playback, but are essentially optional.

Further fields might be added later on to the specification.

### HTTP Headers

In case the streaming server requires them, custom HTTP headers can be set with the following syntax:

```toml
[some-stream]
name = "Example stream"
url = "http://example.com/music.pls"
http_headers = ["User-Agent: your-custom-user-agent", "Foo: goo"]
```

Custom HTTP headers are only supported with the default and recommended `mpv` player.

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

### SMIL

Streams that require CDN tokens generated through an SMIL XML are supported by setting `smil = true`:

```toml
[smil-stream]
name = "Example SMIL stream"
url = "http://example.com/stream/metadata.xml"
smil = true
```

The highest quality stream will be chosen from the highest priority CDN server.
