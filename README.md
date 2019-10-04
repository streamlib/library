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

