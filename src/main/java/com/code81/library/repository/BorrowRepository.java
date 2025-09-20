package com.code81.library.repository;
import com.code81.library.entity.BorrowTransaction;
import org.springframework.data.jpa.repository.JpaRepository;
public interface BorrowRepository extends JpaRepository<BorrowTransaction, Long> { }
