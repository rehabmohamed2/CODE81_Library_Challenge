package com.code81.library.controller;

import com.code81.library.entity.BorrowTransaction;
import com.code81.library.repository.BorrowRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/borrows")
public class BorrowController {
    @Autowired private BorrowRepository repo;

    @GetMapping
    public List<BorrowTransaction> getAll() { return repo.findAll(); }

    @GetMapping("/{id}")
    public ResponseEntity<BorrowTransaction> getById(@PathVariable Long id) {
        Optional<BorrowTransaction> transaction = repo.findById(id);
        if (transaction.isPresent()) {
            return ResponseEntity.ok(transaction.get());
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @PostMapping
    public BorrowTransaction create(@RequestBody BorrowTransaction tx) {
        if (tx.getBorrowDate() == null) {
            tx.setBorrowDate(LocalDate.now());
        }
        return repo.save(tx);
    }

    @PutMapping("/{id}")
    public ResponseEntity<BorrowTransaction> update(@PathVariable Long id, @RequestBody BorrowTransaction txDetails) {
        Optional<BorrowTransaction> optionalTx = repo.findById(id);
        if (optionalTx.isPresent()) {
            BorrowTransaction tx = optionalTx.get();
            tx.setMember(txDetails.getMember());
            tx.setBook(txDetails.getBook());
            tx.setBorrowDate(txDetails.getBorrowDate());
            tx.setReturnDate(txDetails.getReturnDate());
            BorrowTransaction updatedTx = repo.save(tx);
            return ResponseEntity.ok(updatedTx);
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @PutMapping("/{id}/return")
    public ResponseEntity<BorrowTransaction> returnBook(@PathVariable Long id) {
        Optional<BorrowTransaction> optionalTx = repo.findById(id);
        if (optionalTx.isPresent()) {
            BorrowTransaction tx = optionalTx.get();
            if (tx.getReturnDate() == null) {
                tx.setReturnDate(LocalDate.now());
                BorrowTransaction updatedTx = repo.save(tx);
                return ResponseEntity.ok(updatedTx);
            } else {
                return ResponseEntity.badRequest().build();
            }
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
