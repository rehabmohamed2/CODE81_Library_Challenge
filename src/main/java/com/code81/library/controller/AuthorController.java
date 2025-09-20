package com.code81.library.controller;

import com.code81.library.entity.Author;
import com.code81.library.repository.AuthorRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/authors")
public class AuthorController {

    @Autowired
    private AuthorRepository repo;

    @GetMapping
    public List<Author> getAll() {
        return repo.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Author> getById(@PathVariable Long id) {
        Optional<Author> author = repo.findById(id);
        if (author.isPresent()) {
            return ResponseEntity.ok(author.get());
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @PostMapping
    public Author create(@RequestBody Author author) {
        return repo.save(author);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Author> update(@PathVariable Long id, @RequestBody Author authorDetails) {
        Optional<Author> optionalAuthor = repo.findById(id);
        if (optionalAuthor.isPresent()) {
            Author author = optionalAuthor.get();
            author.setName(authorDetails.getName());
            author.setBiography(authorDetails.getBiography());
            author.setNationality(authorDetails.getNationality());
            author.setBirthYear(authorDetails.getBirthYear());
            Author updatedAuthor = repo.save(author);
            return ResponseEntity.ok(updatedAuthor);
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        if (repo.existsById(id)) {
            repo.deleteById(id);
            return ResponseEntity.noContent().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}