package com.code81.library.repository;

import com.code81.library.entity.UserActivity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.List;

@Repository
public interface UserActivityRepository extends JpaRepository<UserActivity, Long> {

    List<UserActivity> findByUserIdOrderByTimestampDesc(Long userId);

    List<UserActivity> findByActionOrderByTimestampDesc(String action);

    @Query("SELECT ua FROM UserActivity ua WHERE ua.timestamp BETWEEN :startDate AND :endDate ORDER BY ua.timestamp DESC")
    List<UserActivity> findByTimestampBetween(@Param("startDate") LocalDateTime startDate, @Param("endDate") LocalDateTime endDate);

    @Query("SELECT ua FROM UserActivity ua WHERE ua.user.id = :userId AND ua.timestamp BETWEEN :startDate AND :endDate ORDER BY ua.timestamp DESC")
    List<UserActivity> findByUserIdAndTimestampBetween(@Param("userId") Long userId, @Param("startDate") LocalDateTime startDate, @Param("endDate") LocalDateTime endDate);
}