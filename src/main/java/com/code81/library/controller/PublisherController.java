package com.code81.library.controller;

import com.code81.library.entity.Publisher;
import com.code81.library.repository.PublisherRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/publishers")
public class PublisherController {

    @Autowired
    private PublisherRepository repo;

    @GetMapping
    public List<Publisher> getAll() {
        return repo.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Publisher> getById(@PathVariable Long id) {
        Optional<Publisher> publisher = repo.findById(id);
        if (publisher.isPresent()) {
            return ResponseEntity.ok(publisher.get());
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @PostMapping
    public Publisher create(@RequestBody Publisher publisher) {
        return repo.save(publisher);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Publisher> update(@PathVariable Long id, @RequestBody Publisher publisherDetails) {
        Optional<Publisher> optionalPublisher = repo.findById(id);
        if (optionalPublisher.isPresent()) {
            Publisher publisher = optionalPublisher.get();
            publisher.setName(publisherDetails.getName());
            publisher.setAddress(publisherDetails.getAddress());
            publisher.setWebsite(publisherDetails.getWebsite());
            publisher.setContactEmail(publisherDetails.getContactEmail());
            publisher.setEstablishedYear(publisherDetails.getEstablishedYear());
            Publisher updatedPublisher = repo.save(publisher);
            return ResponseEntity.ok(updatedPublisher);
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