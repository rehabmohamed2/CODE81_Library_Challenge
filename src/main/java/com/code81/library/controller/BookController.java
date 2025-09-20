package com.code81.library.controller;

import com.code81.library.entity.Book;
import com.code81.library.repository.BookRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/books")
public class BookController {
    @Autowired private BookRepository repo;

    @GetMapping
    public List<Book> getAll() { return repo.findAll(); }

    @GetMapping("/{id}")
    public ResponseEntity<Book> getById(@PathVariable Long id) {
        Optional<Book> book = repo.findById(id);
        if (book.isPresent()) {
            return ResponseEntity.ok(book.get());
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @PostMapping
    public Book create(@RequestBody Book book) { return repo.save(book); }

    @PutMapping("/{id}")
    public ResponseEntity<Book> update(@PathVariable Long id, @RequestBody Book bookDetails) {
        Optional<Book> optionalBook = repo.findById(id);
        if (optionalBook.isPresent()) {
            Book book = optionalBook.get();
            book.setTitle(bookDetails.getTitle());
            book.setIsbn(bookDetails.getIsbn());
            book.setPublicationYear(bookDetails.getPublicationYear());
            book.setEdition(bookDetails.getEdition());
            book.setLanguage(bookDetails.getLanguage());
            book.setSummary(bookDetails.getSummary());
            book.setCoverImageUrl(bookDetails.getCoverImageUrl());
            book.setAuthors(bookDetails.getAuthors());
            book.setPublisher(bookDetails.getPublisher());
            book.setCategory(bookDetails.getCategory());
            Book updatedBook = repo.save(book);
            return ResponseEntity.ok(updatedBook);
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
