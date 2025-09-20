package com.code81.library.repository;
import com.code81.library.entity.Author;
import org.springframework.data.jpa.repository.JpaRepository;
public interface AuthorRepository extends JpaRepository<Author, Long> { }
