import * as React from "react";
import { useEffect, useState } from "react";

const DJANGO_HOST = process.env.DJANGO_HOST || "http://localhost:8000";

type DjangoDog = {
  model: string
  pk: number;
  fields: {
    name: string;
    age:  number;
    my_email: string;
  };
};

type Dog = {
  id: number;
  name: string;
  age: number;
}

const convertDjangoToNormalDog = (djangoDog: DjangoDog): Dog => {
  return {
    id: djangoDog.pk,
    name: djangoDog.fields.name,
    age: djangoDog.fields.age
  }
}

type DogsProps = {
  header?: string
}

type MyForm = {
  header: {value: string}
}

const Dogs = () => {
  const [header, setHeader] = useState("testing")
  const [dogs, setDogs] = useState<Dog[]>([]);

  useEffect(() => {
    fetch(`${DJANGO_HOST}/dogs/`)
      .then((res) => res.json())
      .then((data) => {
        setDogs(data.map(convertDjangoToNormalDog));
      });
  }, []);
  
  const handleClick = () => {
    setHeader("new")
  }

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setHeader(event.target.value)
  }

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const target = event.target as typeof event.target & MyForm;
    console.log(target.header.value)
  }

  return (
    <>
      <h2>{header}</h2>
      <form onSubmit={handleSubmit}>
        <input name="header" onChange={handleChange} value={header} />
      </form>
      <button onClick={handleClick}>Change header</button>
      <ul>
        {dogs.map((dog) => (
          <li key={dog.id}>{dog.name}</li>
        ))}
      </ul>
    </>
  );
};

export default Dogs;
