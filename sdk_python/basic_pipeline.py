import apache_beam as beam

inputs = [0, 1, 2, 3]

with beam.Pipeline() as pipeline:
    outputs = pipeline | "Create initial values" >> beam.Create(inputs)
    outputs | beam.Map(print)
